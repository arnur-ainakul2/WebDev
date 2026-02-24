import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-user',
  template: `
    <p>Username: {{ username }}</p>
    <p>Framework: {{favoriteFramework}}</p>
    <label for="framework">
      Favorite Framework:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
     <label for="username">
       <input id="username" type="text" [(ngModel)]="username"/>
       </label>
    <button (click)="showFramework()">Show Framework</button>
  `,
  imports: [FormsModule],
})
export class User {
  favoriteFramework = '';
  username = '';

  showFramework() {
    alert(this.favoriteFramework);
  }
}
