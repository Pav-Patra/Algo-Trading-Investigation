import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { StockChoice } from '../model/stockChoice.type';

@Injectable({
  providedIn: 'root'
})
export class StockApiService {

  public baseUrl: string = "http://127.0.0.1:8000/stock_choice/";

  http = inject(HttpClient)
  getAllAssets() {
    const httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
    
    return this.http.get<Array<StockChoice>>(this.baseUrl+'assets', {headers: httpHeaders})
  }

}
