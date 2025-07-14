import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { StockApiService } from '../home/stock-api.service';
import { Observable } from 'rxjs';
import { AssetDetails } from '../model/AssetDetails.type';

@Injectable({
  providedIn: 'root'
})
export class AssetsService {

  public baseUrl: string = "http://127.0.0.1:8000/stock_choice/asset/";

  http = inject(HttpClient)
  getAsset(assetName: string) {
     const httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

    return this.http.get<AssetDetails>(this.baseUrl+assetName, { headers: httpHeaders });
  }
}
