import { Component } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  constructor(private toastr: ToastrService) {}
  validarUsuario(usuario: string, contrasena: string) {
    if (usuario != '' && contrasena != '') {
      this.toastr.success('Sesión iniciada con éxito');
    } else {
      this.toastr.error('Usuario no válido');
    }
  }
}
