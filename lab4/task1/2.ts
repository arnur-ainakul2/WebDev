import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: ` Hello {{ city }} on {{ time }} `,
})
export class App {
  city = 'San Francisco';
  time='13:00';
}
