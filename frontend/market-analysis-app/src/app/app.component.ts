import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet , CommonModule, HeaderComponent, FooterComponent],
  providers: [HeaderComponent],
  template: `
    <app-header/>
    <main>
      <router-outlet />
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
