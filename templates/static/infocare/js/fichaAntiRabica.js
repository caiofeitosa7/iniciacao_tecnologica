function check_box(name_class, id_box, change = false) {
  //console.log("#" + name_class + id_box)
  let campos = document.querySelectorAll("." + name_class)
  let state = $("#" + id_box)[0].checked

  //console.log(campos)
  if (change) {
    campos.forEach((element) => {
      if (element.id != id_box)
        document.getElementById(element.id).disabled = !state
    })

    for (let i = 1; i < 3; i++) {
      document.getElementById(campos[i].id).disabled = state
    }
  } else {
    for (let i = 0; i < 3; i++) {
      if (campos[i].id != id_box)
        document.getElementById(campos[i].id).disabled = state
    }
  }
}

function check_boxV2sn(name_class, id_box, change = false) {
  //console.log("#" + name_class + id_box)
  let campos = document.querySelectorAll("." + name_class)
  let state = $("#" + id_box)[0].checked

  //console.log(campos)
  if (change) {
    campos.forEach((element) => {
      if (element.id != id_box)
        document.getElementById(element.id).disabled = !state
    })

    for (let i = 1; i < 2; i++) {
      document.getElementById(campos[i].id).disabled = state
    }
  } else {
    for (let i = 0; i < 2; i++) {
      if (campos[i].id != id_box)
        document.getElementById(campos[i].id).disabled = state
    }
  }
}
