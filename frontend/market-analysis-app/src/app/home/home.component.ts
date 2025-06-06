import { Component } from '@angular/core';
import { StockApiService } from './stock-api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [CommonModule],
  providers: [StockApiService],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

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
