import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CrearComponent } from './crear/crear.component';
import { ListarComponent } from './listar/listar.component';
import { ActualizarComponent } from './actualizar/actualizar.component';
import { EliminarComponent } from './eliminar/eliminar.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'listar',
    component: ListarComponent,
  },
  {
    path: 'crear',
    component: CrearComponent,
  },
  {
    path: 'actualizar',
    component: ActualizarComponent,
  },
  {
    path: 'eliminar',
    component: EliminarComponent,
  },
];

@NgModule({
  declarations: [
    CrearComponent,
    ListarComponent,
    ActualizarComponent,
    EliminarComponent,
  ],
  imports: [CommonModule, RouterModule.forChild(routes)],
})
export class CandidatosModule {}
