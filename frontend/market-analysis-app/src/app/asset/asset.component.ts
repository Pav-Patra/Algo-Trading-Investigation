import { Component, inject, Input } from '@angular/core';
import { AssetsService } from './assets.service';
import { AssetDataService } from '../asset-data.service';

@Component({
  selector: 'app-asset',
  imports: [],
  templateUrl: './asset.component.html',
  styleUrl: './asset.component.css'
})
export class AssetComponent {
  graphHtml: string = '';
  loading: boolean = false;
  error: string = '';
  @Input() assetName = '';
  assetsService = inject(AssetsService)
  fetchedAsset: string = '';

  constructor(private dataService: AssetDataService) {}

  ngOnInit(): void {
    this.dataService.currentData.subscribe(data => {
      this.fetchedAsset = data;
    })
    this.loadAssetGraph(this.fetchedAsset);
  }

  loadAssetGraph(assetName: string) {
    this.loading = true;
    this.assetsService.getAsset(assetName).subscribe()
  }

}
