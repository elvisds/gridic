function Gridic(containerId) {

  var SIZE = 12;
  var DELAY_MS = 250;

  var container = document.getElementById(containerId);

  this.createCell = function(row, col) {
    var cell = document.createElement("div")
    cell.id = "cell-"+row+"-"+col;
    cell.classList.add("cell");
    cell.classList.add("col-" + col);
    cell.row = row;

    cell.onclick = function() {
      this.classList.toggle("selected");
    }
    return cell;
  }

  this.createRow = function(id) {
    var row = document.createElement("div");
    row.id = "row-" + id;
    row.classList.add("row");

    for (var col=0; col<SIZE; col++) {
      row.appendChild(this.createCell(id,col));
    }
    return row;
  }

  this.draw = function() {
    for (var row=0; row<SIZE; row++) {
      container.appendChild(this.createRow(row));
    }
  }

  this.selectedColumn = 0;

  this.setColumnActive = function(column, isActive) {
    var cells = document.querySelectorAll(".col-" + column);

    _.each(cells, function(el) {
      if (isActive) {
        el.classList.add("active");
      } else {
        el.classList.remove("active");
      }
    });
  }

  this.playColumn = function(column) {
    var notes = _.pluck(document.querySelectorAll(".col-" + 
      column + ".selected"), "row").join(",");
    if (notes.length > 0) {
      var url = "/play?notes=" + notes;
      console.log(url);
      var xhReq = new XMLHttpRequest();
      xhReq.open("GET", url, false);
      xhReq.send(null);
    }
  }

  this.playNextColumn = function() {
    this.setColumnActive(this.selectedColumn, false);
    this.selectedColumn = (this.selectedColumn + 1) % SIZE;
    this.setColumnActive(this.selectedColumn, true);
    this.playColumn(this.selectedColumn);
  }

  this.looper = null;

  this.activate = function() {
    var that = this;
    this.looper = setInterval(function(){
      that.playNextColumn();
    }, DELAY_MS);
  }

  this.draw();
}