var config = {
  '#id_requisitos'           : {
      no_results_text: 'No se encontro la materia',
      width: '70%',
      disable_search_threshold: 10,
      placeholder_text_multiple: "Requisitos"
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
