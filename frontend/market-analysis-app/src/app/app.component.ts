import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StockApiService } from './stock-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  imports: [CommonModule],
  styleUrl: './app.component.css',
  providers: [StockApiService]
})
export class AppComponent {
  title = 'market-analysis-app';

  

  public base_url: string;

  constructor(private stockApiService: StockApiService) {
    this.base_url = this.stockApiService.baseUrl;

    this.getAllAssets();
  }

  stock_list = [
    {key: 'TS', name: 'Test'}
  ];

  getAllAssets = () => {
    this.stockApiService.getAllAssets().subscribe({
      next: (data) => this.stock_list = data ,
      error: (error) => console.log(error),
      complete: () => console.info('complete')
    })
  }
 
  
}
