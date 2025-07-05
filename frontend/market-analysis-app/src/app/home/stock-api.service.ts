import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AssetChoice } from '../model/AssetChoice.type';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StockApiService {

  public baseUrl: string = "http://127.0.0.1:8000/stock_choice/";

  http = inject(HttpClient)
  getAllAssets(): Observable<Array<AssetChoice>> {
    const httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
    
    return this.http.get<Array<AssetChoice>>(this.baseUrl+'assets', {headers: httpHeaders})
  }

}
