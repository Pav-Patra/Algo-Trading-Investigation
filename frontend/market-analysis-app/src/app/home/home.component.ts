import { Component, inject, OnInit, signal } from '@angular/core';
import { StockApiService } from './stock-api.service';
import { CommonModule } from '@angular/common';
import { catchError } from 'rxjs';
import { StockChoice } from '../model/stockChoice.type';

@Component({
  selector: 'app-home',
  imports: [CommonModule],
  providers: [StockApiService],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {

  stockApiService = inject(StockApiService);
  stockList = signal<Array<StockChoice>>([]);
  baseUrl = signal<String>("");

  ngOnInit(): void {
    this.baseUrl.set(this.stockApiService.baseUrl);
    this.stockApiService.getAllAssets().pipe(
      catchError((err) => {
        console.log(err);
        throw err;
      })
    )
    .subscribe((assets) => {
      this.stockList.set(assets);
    })
  }

}
