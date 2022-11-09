package proyecto.grupo29.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import proyecto.grupo29.seguridad.Modelos.Permiso;
import proyecto.grupo29.seguridad.Repositorios.RepositorioPermiso;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @GetMapping("")
    public List<Permiso> index() {
        return this.miRepositorioPermiso.findAll();
    }

    @GetMapping("{id}")
    public Permiso show(@PathVariable String id) {
        return this.miRepositorioPermiso.findById(id).orElse(null);
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Permiso create(@RequestBody Permiso infoPermiso) {
        return this.miRepositorioPermiso.save(infoPermiso);
    }

    @PutMapping("{id}")
    public Permiso update(@RequestBody Permiso infoPermiso, @PathVariable String id){
        Permiso permisoActual = this.miRepositorioPermiso.findById(id).orElse(null);
        if (permisoActual!=null && infoPermiso!=null){
            permisoActual.setMetodo(infoPermiso.getMetodo());
            permisoActual.setUrl(infoPermiso.getUrl());
            return this.miRepositorioPermiso.save(permisoActual);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Permiso permisoActual = this.miRepositorioPermiso.findById(id).orElse(null);
        if(permisoActual!= null){
            this.miRepositorioPermiso.delete(permisoActual);
        }
    }
}
