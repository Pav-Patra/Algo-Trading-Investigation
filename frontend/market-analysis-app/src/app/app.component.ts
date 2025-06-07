import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from "./home/home.component";
import { FooterComponent } from './footer/footer.component';

@Component({
  selector: 'app-root',
  imports: [CommonModule, HeaderComponent, HomeComponent, FooterComponent],
  providers: [HeaderComponent],
  template: `
    <app-header/>
    <main>
      <app-home/>
    </main>
    <app-footer/>
    
  `,
  styles: [
    `
      main {
        flex: 1;
        padding: 16px;
      }
    `
  ]
})
export class AppComponent {
  title = 'market-analysis-app';
 
}
