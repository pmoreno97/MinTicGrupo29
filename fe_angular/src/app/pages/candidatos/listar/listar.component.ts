import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';
import { Candidato } from '../../../modelos/candidato/candidato.model';
import { CandidatoService } from '../../../servicios/candidato.service';

@Component({
  selector: 'app-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.css'],
})
export class ListarComponent implements OnInit {
  candidatos: Candidato[] = [];
  nombresColumnas: string[] = ['Cedula', 'Nombre', 'Apellido', 'Opciones'];
  constructor(private miServicioCandidatos: CandidatoService) {}

  ngOnInit(): void {
    this.listar();
  }
  listar(): void {
    this.miServicioCandidatos.listar().subscribe((data) => {
      this.candidatos = data;
    });
  }
  agregar(): void {
    console.log('agregando nuevo');
  }
  editar(id: string): void {
    console.log('editando a ' + id);
  }
  eliminar(id: string): void {
    Swal.fire({
      title: 'Eliminar Candidato',
      text: 'Está seguro que quiere eliminar el candidato?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar',
    }).then((result) => {
      if (result.isConfirmed) {
        this.miServicioCandidatos.eliminar(id).subscribe((data) => {
          Swal.fire(
            'Eliminado!',
            'El candidato ha sido eliminada correctamente',
            'success'
          );
          this.ngOnInit();
        });
      }
    });
  }
}
