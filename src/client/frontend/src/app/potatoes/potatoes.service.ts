import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Potato } from './potato.interface';

@Injectable({
  providedIn: 'root'
})
export class PotatoesService {

  constructor(
    private http: HttpClient
  ) { }

  getPotatoes() {
    return this.http.get<Potato[]>('http://localhost:8002/potatoes')
  }
}
