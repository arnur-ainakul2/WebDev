import {Component} from '@angular/core';
import {RouterOutlet,RouterLink} from '@angular/router';

@Component({
  imports:[RouterOutlet,RouterLink],
  selector: 'app-root',
  template: `
    <nav>
      <a routerLink="/">Home</a>
      |
      <a routerLink="/user">User</a>
    </nav>
    <router-outlet />
  `,
})
export class App {}
