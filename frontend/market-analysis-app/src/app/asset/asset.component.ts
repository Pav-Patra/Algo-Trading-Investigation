import { AfterViewInit, Component, ElementRef, inject, Input, OnInit, signal, ViewChild } from '@angular/core';
import { AssetsService } from './assets.service';
import { catchError } from 'rxjs';
import { AssetDataService } from '../asset-data.service';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);
 
@Component({
  selector: 'app-asset',
  standalone: true,
  imports: [],
  templateUrl: './asset.component.html',
  styleUrl: './asset.component.css'
})
export class AssetComponent implements OnInit {

  graphHtml = signal<SafeHtml>("");
  loading: boolean = false;
  error: string = '';
  @Input() assetName = '';
  assetsService = inject(AssetsService)
  fetchedAsset = signal<string>("");


  constructor(private dataService: AssetDataService, private sanitizer: DomSanitizer) {}

  public config: any = {
    type: 'bar',

    data: {
      labels: ['JAN', 'FEB', 'MAR', 'APRIL'],
      datasets:[
        {
          label: 'Sales',
          data: ['467', '576', '572', '588'],
          backgroundColor: 'blue' 
        },
        {
          label: 'PAT',
          data: ['100', '120', '133', '134'],
          backgroundColor: 'red' 
        },
      ],
    },
    options: {
      aspectRatio: 1,
    },
  };
  chart: any;

  ngOnInit() {
    this.dataService.currentData.subscribe(data => {
      this.fetchedAsset.set(data);
    });
    this.chart = new Chart('MyChart', this.config);
    this.loadAssetGraph(this.fetchedAsset());
  }

  loadAssetGraph(assetName: string) {
    this.loading = true;
    this.assetsService.getAsset(assetName).pipe(
      catchError((err) => {
        console.log(err);
        throw err;
      })
    )
    .subscribe((graph) => {
      console.log(graph.graphHtml)
      this.graphHtml.set(this.sanitizer.bypassSecurityTrustHtml(graph.graphHtml))
    })
  }

}
