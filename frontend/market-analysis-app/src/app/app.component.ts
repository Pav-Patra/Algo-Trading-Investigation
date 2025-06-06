import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from "./home/home.component";

@Component({
  selector: 'app-root',
  imports: [CommonModule, HeaderComponent, HomeComponent],
  providers: [HeaderComponent],
  template: `
    <app-header/>
    <main>
      <app-home/>
    </main>
    
  `,
  styles: [
    `
      main {
        padding: 16px;
      }
    `
  ]
})
export class AppComponent {
  title = 'market-analysis-app';
 
}
