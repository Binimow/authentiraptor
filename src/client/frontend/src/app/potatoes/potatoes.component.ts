import { Component } from '@angular/core';
import { PotatoesService } from './potatoes.service';
import { Potato } from './potato.interface';

@Component({
  selector: 'app-potatoes',
  templateUrl: './potatoes.component.html',
  styleUrls: ['./potatoes.component.css']
})
export class PotatoesComponent {
  constructor(
    private potatoesService: PotatoesService,
  ) { }

  potatoes: Potato[] = []

  getPotatoList() {
    this.potatoesService.getPotatoes().subscribe(potatoes => {
      this.potatoes = potatoes
    })
  }
}
