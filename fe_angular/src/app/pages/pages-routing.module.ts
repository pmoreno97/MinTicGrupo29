import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';

const routes: Routes = [
  {
    path: '',
    component: PagesComponent,
    children: [
      {
        path: 'seguridad',
        loadChildren: () =>
          import('./seguridad/seguridad.module').then((m) => m.SeguridadModule),
      },
      {
        path: 'usuarios',
        loadChildren: () =>
          import('./usuarios/usuarios.module').then((m) => m.UsuariosModule),
      },
      {
        path: 'candidatos',
        loadChildren: () =>
          import('./candidatos/candidatos.module').then(
            (m) => m.CandidatosModule
          ),
      },
      {
        path: 'mesas',
        loadChildren: () =>
          import('./mesas/mesas.module').then((m) => m.MesasModule),
      },
      {
        path: 'resultados',
        loadChildren: () =>
          import('./resultados/resultados.module').then(
            (m) => m.ResultadosModule
          ),
      },
      {
        path: 'reportes',
        loadChildren: () =>
          import('./reportes/reportes.module').then((m) => m.ReportesModule),
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule {}
