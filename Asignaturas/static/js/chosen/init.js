var config = {
  '#id_requisitos'           : {
      no_results_text: 'No se encontro la materia',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Requisitos"
  },
    '#id_asignaturas'           : {
      no_results_text: 'No se encontro la materia',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Asignaturas"
  },
    '#id_disponibilidad'           : {
      no_results_text: 'No se encontro el bloque',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Disponibilidad"
  },
    '#profesores_oferta'           : {
      no_results_text: 'No se encontro el profesor',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Profesores"
  },
    '#id_preferencias'           : {
      no_results_text: 'No se encontro la materia',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Materias"
  },
  // '.chosen-select-deselect'  : { allow_single_deselect: true },
  // '.chosen-select-no-single' : { disable_search_threshold: 10 },
  // '.chosen-select-no-results': { no_results_text: 'Oops, nothing found!' },
  // '.chosen-select-rtl'       : { rtl: true },
  // '.chosen-select-width'     : { width: '95%' }
}
for (var selector in config) {
  $(selector).chosen(config[selector]);
}
