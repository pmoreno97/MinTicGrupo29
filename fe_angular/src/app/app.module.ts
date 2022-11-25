import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ResultadosComponent } from './resultados/resultados.component';
import { ReportesComponent } from './reportes/reportes.component';
import { LoginComponent } from './login/login.component';
import { MesasComponent } from './mesas/mesas.component';
import { CandidatosComponent } from './candidatos/candidatos.component';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'candidatos', component: CandidatosComponent },
  { path: 'mesas', component: MesasComponent },
  { path: 'resultados', component: ResultadosComponent },
  { path: 'reportes', component: ReportesComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ResultadosComponent,
    ReportesComponent,
    LoginComponent,
  ],
  imports: [BrowserModule, FontAwesomeModule, RouterModule.forRoot(appRoutes)],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
