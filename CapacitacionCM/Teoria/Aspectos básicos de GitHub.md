
https://learn.microsoft.com/es-es/training/paths/github-administration-products/


# Introducción a GitHub

Entre las características clave que ofrece GitHub se incluyen las siguientes:

-   Issues
-   Debates
-   Solicitudes de incorporación de cambios
-   Notificaciones
-   Etiquetas
	- Estos son algunos ejemplos de etiquetas:
		-   error
		-   en línea
		-   duplicar
		-   help-wanted
		-   mejora
		-   question

-   Acciones
	- Acciones de GitHub se compone de lo siguiente:
		-   **Flujos de trabajo**: procesos automatizados que se han agregado al repositorio.
		-   **Eventos**: actividades que desencadenan un flujo de trabajo.
		-   **Trabajos**: conjunto de pasos que se ejecutan en un ejecutor.
		-   **Pasos**: tarea que puede ejecutar uno o varios comandos (acciones).
		-   **Acciones**: comandos independientes que se pueden combinar en pasos. Se pueden combinar varios pasos para crear un trabajo.
		-   **Ejecutores**: servidor que tiene instalada la aplicación de ejecutor de Acciones de GitHub.
	
-   Horquillas
-   Proyectos


## Clonación y bifurcación
![La bifurcación de un repositorio crea una copia de este en su cuenta de GitHub. Después, puede clonar la copia bifurcada del repositorio en el equipo local.](https://learn.microsoft.com/es-es/training/github/introduction-to-github/media/2-fork-clone.png)

![Los cambios locales pueden insertarse en el repositorio de origen y, luego, se puede crear una solicitud de incorporación de cambios para obtener los cambios en el repositorio ascendente.](https://learn.microsoft.com/es-es/training/github/introduction-to-github/media/2-fork-pullrequest.png)


## GitHub Pages

![GitHub Pages es un motor de hospedaje que está disponible en la cuenta de GitHub. Se puede usar para hospedar sitios estáticos generados desde el repositorio.](https://learn.microsoft.com/es-es/training/github/introduction-to-github/media/2-github-pages.png)




### Exam

![[Pasted image 20230412102233.png]]


# Introducción a la administración de GitHub

### Administración en el nivel de equipo

![Captura de pantalla de la pantalla de la organización con la pestaña Equipos resaltada.](https://learn.microsoft.com/es-es/training/github/github-introduction-administration/media/teams.png)

-   Cree un equipo y seleccione o cambie el equipo principal.
-   Eliminar un equipo o cambiarle el nombre.
-   Agregar miembros de la organización a un equipo o quitarlos de este, así como sincronizar la pertenencia de un equipo de GitHub con un grupo de IdP.
-   Agregue o quite colaboradores externos (personas que no sean explícitamente miembros de su organización, como consultores o empleados temporales) de los repositorios de equipo.
-   Habilite o deshabilite las discusiones del equipo en la página del equipo.
-   Cambiar la visibilidad del equipo dentro de la organización.
-   Administrar la asignación automática de revisión de código para las solicitudes de incorporación de cambios mediante el algoritmo de enrutamiento de asignación de revisión de GitHub.
-   Programe recordatorios.
-   Configure la imagen de perfil de su equipo.



## Administración de nivel de organización

-   Invite a usuarios a unirse a la organización y quite miembros de la organización.
-   Organizar a los usuarios en un equipo y conceder permisos de "responsable de mantenimiento del equipo" a los miembros de la organización.
-   Agregue o quite colaboradores externos (personas que no sean explícitamente miembros de su organización, como consultores o empleados temporales) de los repositorios de la organización.
-   Conceder niveles de permisos de repositorio a miembros y establecer el nivel de permiso base (predeterminado) para un repositorio determinado.
-   Configurar la seguridad de la organización.
-   Configurar la facturación o asignar un administrador de facturación para la organización.
-   Extraiga varios tipos de información sobre los repositorios mediante el uso de scripts personalizados.
-   Aplique cambios en toda la organización, como las migraciones, mediante el uso de scripts personalizados.
- -   No es posible duplicar una organización ni compartir configuraciones entre dos organizaciones. Esto significa que debe configurar todo desde cero cada vez que cree una organización, lo que aumenta el riesgo de errores en la configuración.
-   En función de las directivas de los proveedores de software, podría incurrir en costos adicionales si necesita instalar algunas aplicaciones en varias organizaciones.
-   La administración de varias organizaciones suele ser más difícil.


## ¿Cómo funciona la autenticación de GitHub?


### Opciones de autenticación de GitHub

Nombre de usuario y contraseña
Tokens de acceso personal ![Captura de pantalla de la pantalla de token de acceso personal.](https://learn.microsoft.com/es-es/training/github/github-introduction-administration/media/personal-access-token.png)
Claves SSH
Claves de implementación

### Opciones de seguridad agregadas de GitHub

#### Autenticación en dos fases ![Captura de pantalla de la pantalla de autenticación en dos fases.](https://learn.microsoft.com/es-es/training/github/github-introduction-administration/media/2-factor-authentication.png)

#### SSO de SAML
-   Azure Active Directory (Azure AD)
-   Okta
-   OneLogin
-   PingOne

## exam
![[Pasted image 20230412111959.png]]


# Introducción a los productos de GitHub

## Enfoque en los productos de GitHub

#### GitHub Free

-   Repositorios públicos o privados ilimitados
-   2000 minutos de automatización de acciones al mes (_gratis para repositorios públicos_)
-   500 MB de almacenamiento de paquetes (_gratis para repositorios públicos_)
-   120 horas principales de proceso de Codespaces/mes
-   15 GB de almacenamiento de Codespaces/mes
-   Nuevos problemas y proyectos (en versión beta limitada)
-   Soporte técnico de la comunidad de GitHub
-   Alertas de Dependabot
-   Aplicación de la autenticación en dos fases

#### GitHub Pro
		GitHub Pro incluyen todas las características de una cuenta de GitHub Free, además de las características avanzadas siguientes:

-   Soporte técnico de GitHub por correo electrónico.
-   Necesidad de revisores de solicitudes de incorporación de cambios
-   Varios revisores de solicitudes de incorporación de cambios
-   Referencias vinculadas automáticamente
-   GitHub Pages
-   Wikis
-   Ramas protegidas
-   Propietarios del código
-   Gráficos de conclusiones del repositorio
	
Además, GitHub Pro aumenta los límites de Acciones de GitHub y Paquetes de GitHub para repositorios privados.

Minutos de Acciones de GitHub = 3000
Almacenamiento de Paquetes de GitHub = 2 GB
Horas principales de GitHub Codespaces = 180
Almacenamiento de GitHub Codespaces = 20 GB

#### GitHub Team

es la versión de GitHub Pro para organizaciones, Incluye todas las características de GitHub Pro.

-   Borrador de solicitudes de incorporación de cambios
-   Revisores de solicitudes de incorporación de cambios en equipo
-   Avisos programados
	
#### GitHub Enterprise

-   Soporte técnico para GitHub Enterprise
-   Más controles de seguridad, cumplimiento e implementación
-   Autenticación con inicio de sesión único de SAML
-   Acceso al aprovisionamiento con SAML o SCIM
-   GitHub Connect
-   La opción de comprar GitHub Advanced Security


lista de los tres tipos de cuentas de GitHub

-   Cuentas de usuario personales
-   Cuentas de organización
-   Cuenta de empresa

## Licencias para productos de uso medidor

