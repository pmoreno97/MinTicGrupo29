import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  private usuarioRegistrado = false;
  private anuncio: string = 'Se registró a ';

  frutas: string[] = ['aguacate', 'mango', 'fresa', 'piña'];
  setUsuarioRegistrado() {
    this.usuarioRegistrado = true;
  }
  getUsuarioRegistrado() {
    return this.usuarioRegistrado;
  }

  setAnuncio(nombre: string) {
    this.anuncio += nombre;
  }
  getAnuncio() {
    return this.anuncio;
  }

  registrarUsuario(nombre: string) {
    if (nombre != '') {
      this.setUsuarioRegistrado();
      this.setAnuncio(nombre);
    }
  }
}
