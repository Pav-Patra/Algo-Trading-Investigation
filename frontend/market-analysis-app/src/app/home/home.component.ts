import { Component, inject, OnInit, signal } from '@angular/core';
import { StockApiService } from './stock-api.service';
import { CommonModule } from '@angular/common';
import { catchError, forkJoin } from 'rxjs';
import { AssetChoice } from '../model/AssetChoice.type';
import { RouterLink } from '@angular/router';
import { AssetDataService } from '../asset-data.service';


@Component({
  selector: 'app-home',
  imports: [CommonModule, RouterLink],
  providers: [StockApiService],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {

  stockApiService = inject(StockApiService);
  assetMap = signal<{ [assetKey: string]: AssetChoice }>({});
  baseUrl = signal<String>("");

  constructor(private dataService: AssetDataService) {}

  sendData(asset: string) {
    this.dataService.updateData(asset)
  }

  ngOnInit(): void {
    this.baseUrl.set(this.stockApiService.baseUrl);

    // initialise for 1 week percentage change
    this.loadAssetsAndChanges(10080);
  }

  loadAssetsAndChanges(minutes: number): void {
    forkJoin({
      assets: this.stockApiService.getAllAssets(),
      changes: this.stockApiService.getAllAssetPercentageChange(minutes)
    }).subscribe(({assets,changes}) => {
      const map: { [key: string]: AssetChoice } = {};

      // build initial map for asset names
      assets.forEach(asset => {
        map[asset.key] = {
          key: asset.key,
          name: asset.name,
          percentChange: 0
        };
      });

      // overlay percentage changes
      changes.forEach(change => {
        if (map[change.key]) {
          map[change.key].percentChange = Number(change.percentChange.toFixed(2));
        }
      });

      this.assetMap.set(map);
    });
  };

  get assetEntries() {
    return Object.entries(this.assetMap()).map(([key, value]) => ({
    key,
    value
  }));
  }

}
