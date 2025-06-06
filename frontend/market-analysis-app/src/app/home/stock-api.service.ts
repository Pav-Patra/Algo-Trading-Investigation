import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StockApiService {

  public baseUrl: string = "http://127.0.0.1:8000/stock_choice/";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  getAllAssets(): Observable<any> {
    return this.http.get(this.baseUrl + 'assets', 
      {headers: this.httpHeaders})
  }
}
