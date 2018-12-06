$(document).ready(function() {
    $('#example').DataTable( {
        "language": {
            "lengthMenu": "Ver _MENU_ asignaturas por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron asignaturas",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay asignaturas disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total asignaturas registradas)",
            "search":         "Buscar   :"
        },
        "order": [[1, 'desc']],
        "columns": [
            null,
            null,
            null,
            null,
            null,
            { "orderable": false},
            { "orderable": false}
        ],
    } );
  } );



