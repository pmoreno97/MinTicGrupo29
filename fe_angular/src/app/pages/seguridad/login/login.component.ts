import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Usuario } from '../../../modelos/usuario/usuario.model';
import { SeguridadService } from '../../../servicios/seguridad.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  correo: string = '';
  contrasena: string = '';
  constructor(
    private toastr: ToastrService,
    private miServicioSeguridad: SeguridadService,
    private router: Router
  ) {}

  /**
   * Método que se ejecuta una vez se carga la página
   */
  ngOnInit(): void {}
  /**
   * Este método permite llevar a cabo el proceso de login,
   * llamando al método correspondiente de los servicios
   * para solicitar la validación al backend
   */
  login(): void {
    console.log('aqui' + this.correo + ' contraseña ' + this.contrasena);
    let elUsuario: Usuario = {
      correo: this.correo,
      contrasena: this.contrasena,
    };
    this.miServicioSeguridad.login(elUsuario).subscribe(
      (data) => {
        this.router.navigate(['pages/dashboard']);
        this.miServicioSeguridad.guardarDatosSesion(data);
      },
      (error) => {
        this.toastr.success('Error durante el login', 'Error');
      }
    );
  }
}
