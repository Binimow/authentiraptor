import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PotatoesComponent } from './potatoes/potatoes.component';
import { GetAccessTokenComponent } from './authorization/access-token-button/access-token-button.component';


@NgModule({
  declarations: [
    AppComponent,
    PotatoesComponent,
    GetAccessTokenComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
