import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';
import { Mesa } from '../../../modelos/mesa/mesa.model';
import { MesaService } from '../../../servicios/mesa.service';

@Component({
  selector: 'app-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.css'],
})
export class ListarComponent implements OnInit {
  mesas: Mesa[] = [];
  nombresColumnas: string[] = ['numero', 'cantidad_inscritos', 'Opciones'];
  constructor(private miServicioMesas: MesaService) { }

  ngOnInit(): void {
    this.listar();
  }
  listar(): void {
    this.miServicioMesas.listar().subscribe((data) => {
      this.mesas = data;
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
      title: 'Eliminar mesa',
      text: 'Está seguro que quiere eliminar la mesa?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar',
    }).then((result) => {
      if (result.isConfirmed) {
        this.miServicioMesas.eliminar(id).subscribe((data) => {
          Swal.fire(
            'Eliminado!',
            'La mesa ha sido eliminada correctamente',
            'success'
          );
          this.ngOnInit();
        });
      }
    });
  }
}
