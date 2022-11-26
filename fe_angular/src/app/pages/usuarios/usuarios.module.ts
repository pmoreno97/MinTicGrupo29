import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListarComponent } from './listar/listar.component';
import { CrearComponent } from './crear/crear.component';
import { RouterModule, Routes } from '@angular/router';

const appRoutes: Routes = [
  {
    path: 'usuarios/listar',
    component: ListarComponent,
  },
  {
    path: 'usuarios/crear',
    component: CrearComponent,
  },
];

@NgModule({
  declarations: [ListarComponent, CrearComponent],
  imports: [CommonModule, RouterModule.forChild(appRoutes)],
})
export class UsuariosModule {}
