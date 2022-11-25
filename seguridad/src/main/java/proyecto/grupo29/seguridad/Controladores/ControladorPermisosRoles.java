package proyecto.grupo29.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import proyecto.grupo29.seguridad.Modelos.Permiso;
import proyecto.grupo29.seguridad.Modelos.PermisosRoles;
import proyecto.grupo29.seguridad.Modelos.Rol;
import proyecto.grupo29.seguridad.Repositorios.RepositorioPermiso;
import proyecto.grupo29.seguridad.Repositorios.RepositorioPermisosRoles;
import proyecto.grupo29.seguridad.Repositorios.RepositorioRol;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class ControladorPermisosRoles {
    @Autowired
    private RepositorioPermisosRoles miRepositorioPermisosRoles;
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<PermisosRoles> index(){
        return this.miRepositorioPermisosRoles.findAll();
    }

    @GetMapping("{id}")
    public PermisosRoles show(@PathVariable String id){
        return this.miRepositorioPermisosRoles.findById(id).orElse(null);
    }

    /**
     *
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles create(@PathVariable String id_rol, @PathVariable String id_permiso){
        PermisosRoles nuevo = new PermisosRoles();
        Rol elRol = this.miRepositorioRol.findById(id_rol).orElse(null);
        Permiso elPermiso = this.miRepositorioPermiso.findById(id_permiso).orElse(null);
        if (elRol!=null || elPermiso!=null){
            nuevo.setRol(elRol);
            nuevo.setPermiso(elPermiso);
            return this.miRepositorioPermisosRoles.save(nuevo);
        } else {
            return null;
        }
    }

    /**
     *
     * @param id
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles update(@PathVariable String id, @PathVariable String id_rol, @PathVariable String id_permiso){
        PermisosRoles permisoRolActual = this.miRepositorioPermisosRoles.findById(id).orElse(null);
        Permiso elPermiso = this.miRepositorioPermiso.findById(id_permiso).orElse(null);
        Rol elRol = this.miRepositorioRol.findById(id_rol).orElse(null);
        if(permisoRolActual!=null && elPermiso!=null && elRol!=null){
            permisoRolActual.setRol(elRol);
            permisoRolActual.setPermiso(elPermiso);
            return this.miRepositorioPermisosRoles.save(permisoRolActual);
        } else {
            return null;
        }

    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisosRoles permisoRolActual = this.miRepositorioPermisosRoles.findById(id).orElse(null);
        if (permisoRolActual!=null){
            this.miRepositorioPermisosRoles.delete(permisoRolActual);
        }
    }

    @GetMapping("validar-permiso/rol/{id_rol}")
    public PermisosRoles getPermiso(@PathVariable String id_rol,@RequestBody
    Permiso infoPermiso){
        Permiso elPermiso=this.miRepositorioPermiso
                .getPermiso(infoPermiso.getUrl(),
                        infoPermiso.getMetodo());
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        if (elPermiso!=null && elRol!=null){
            return
                    this.miRepositorioPermisosRoles.getPermisoRol(elRol.get_id(),elPermiso.get_id());
        }else{
            return null;
        }
    }


}
