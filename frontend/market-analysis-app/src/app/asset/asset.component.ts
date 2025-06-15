import { Component, inject } from '@angular/core';
import { AssetsService } from './assets.service';

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
  assetsService = inject(AssetsService)

  ngOnInit(): void {
    this.loadAssetGraph();
  }

  loadAssetGraph(assetName: string) {
    this.loading = true;
    this.assetsService.getAsset(assetName).subscribe()
  }

}
