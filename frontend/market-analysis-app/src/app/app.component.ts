import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StockApiService } from './stock-api.service';
import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  imports: [CommonModule, HeaderComponent],
  providers: [StockApiService, HeaderComponent],
  template: `
    <app-header />

    <div class="btn-group">
        <div *ngFor="let stock of stock_list">
            <a href="{{ base_url }}asset/{{ stock.key }}/">
                <button>
                    {{ stock.name }}
                </button>
            </a>
        </div>
    </div>
  `,
  styles: [
    
  ]
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
