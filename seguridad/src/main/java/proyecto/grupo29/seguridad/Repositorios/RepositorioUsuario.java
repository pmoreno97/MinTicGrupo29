package proyecto.grupo29.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import proyecto.grupo29.seguridad.Modelos.Usuario;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
}
