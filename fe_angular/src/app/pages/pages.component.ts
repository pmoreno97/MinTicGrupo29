import { Component } from '@angular/core';

import { faUser } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'pages',
  templateUrl: './pages.component.html',
})
export class PagesComponent {
  faUser = faUser;
}
