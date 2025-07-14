import { AfterViewInit, Component, ElementRef, inject, Input, OnInit, signal, ViewChild } from '@angular/core';
import { AssetsService } from './assets.service';
import { catchError } from 'rxjs';
import { AssetDataService } from '../asset-data.service';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { Chart, ChartConfiguration, ChartType, registerables } from 'chart.js';
 
@Component({
  selector: 'app-asset',
  standalone: true,
  imports: [],
  templateUrl: './asset.component.html',
  styleUrl: './asset.component.css'
})
export class AssetComponent implements OnInit {
  @ViewChild('chartCanvas', { static: true }) chartCanvas!: ElementRef<HTMLCanvasElement>;

  graphHtml = signal<SafeHtml>("");
  loading: boolean = false;
  error: string = '';
  @Input() assetName = '';
  assetsService = inject(AssetsService)
  fetchedAsset = signal<string>("");
  closingPrices: number[] = []
  assetDates: string[] = []

  private chart ?: Chart;


  constructor(private dataService: AssetDataService, private sanitizer: DomSanitizer) {
    Chart.register(...registerables);
  }

  ngOnInit() {
    this.dataService.currentData.subscribe(data => {
      this.fetchedAsset.set(data);
    });
    this.loadAssetGraph(this.fetchedAsset());
  }

  private loadAssetGraph(assetName: string) {
    this.loading = true;
    this.assetsService.getAsset(assetName).pipe(
      catchError((err) => {
        console.log(err);
        throw err;
      })
    )
    .subscribe((graph) => {
      console.log(graph.graphHtml);
      this.graphHtml.set(this.sanitizer.bypassSecurityTrustHtml(graph.graphHtml));
      this.closingPrices = graph.assetClosingPrices;
      this.assetDates = graph.assetDates;
      console.log(this.closingPrices)
      console.log(this.assetDates)

      this.createChart();
    })
  };

  private createChart(): void {
    const ctx = this.chartCanvas.nativeElement.getContext('2d');
    if(!ctx) return;

    const config: ChartConfiguration = {
      type: 'line' as ChartType,
      data: {
        labels: this.assetDates,
        datasets: [{
          label: 'Closing Price',
          data: this.closingPrices,
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          tension: 0.1,
          fill: true
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        aspectRatio: 2,
        scales: {
          x: {
            type: 'category',
            title: {
              display: true,
              text: 'Date'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Price'
            }
          }
        },
        plugins: {
          title: {
            display: true,
            text: 'Asset Price Over Time'
          },
          legend: {
            display: true,
            position: 'top'
          }
        }
      }
    };
    this.chart = new Chart(ctx, config);
  }

  // Helper method to get date range
  getDateRange(): string {
    if (this.assetDates.length === 0) return 'No data';
    const start = this.assetDates[0];
    const end = this.assetDates[this.assetDates.length - 1];
    return `${start} to ${end}`;
  }

}
