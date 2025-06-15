import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { StockApiService } from '../home/stock-api.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AssetsService {

  public baseUrl: string = "http://127.0.0.1:8000/stock_choice/";

  http = inject(HttpClient)
  getAsset(assetName: string): Observable<string> {
    return this.http.get(this.baseUrl+assetName, { responseType: 'text' });
  }
}
