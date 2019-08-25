const addTicketRow = function () {
    $(".menu-button").on("click", function() {
        const table = document.getElementById("ticket-table");
        const row = table.insertRow();
        const td1 = row.insertCell(0);
        const td2 = row.insertCell(1);
        const td3 = row.insertCell(2);

        td1.className = "ticket-qty"
        td2.className = "ticket-item"
        td3.className = "ticket-price"

        console.log(this)
        console.log(this.children)
        console.log(this.children[1])
        console.log(this.children[1].textContent)
        console.log(this.children[1].value)

        td1.innerHTML = '1'
        td2.innerHTML = this.children[1].textContent
        td3.innerHTML = this.value
    })
}

// TODO: Fix This
function deleteTicketRow() {
    const table = document.getElementById("ticket-table");
    rowSelected = table.getElementsByTagName('tr');
    for (row = 0; row < rowSelected; row++) {
        if (row.hasAttribute('highlight')) {
            table.deleteRow(row)
        }
    }
}

const addMenuButton = function(value) {
    const element = document.getElementById('menu-items');
    const button = document.createElement('button');
    const span = document.createElement('span');

    value = "7.50"
    button.setAttribute('class', 'btn btn-block menu-button');
    button.setAttribute('value', value);
    span.setAttribute('class', 'menu-button-text');

    $("#add-menu-item").on("click", function () {
        element.appendChild(button);
        button.appendChild(span);
        
    })
}

// function highlightTicketRow() {
//     let highlighter = "#ccff00"
//     const table = document.getElementById("ticket-table");
//     const cells = table.getElementsByTagName('td');

//     for (var i = 0; i < cells.length; i++) {
//         var cell = cells[i]
//         cell.onclick = function () {
//             var rowId = this.parentNode.rowIndex;

//             // Makes sure to clear all non-highlighted rows
//             var rowsNotSelected = table.getElementsByTagName('tr');
//             for (var row = 0; row < rowsNotSelected.length; row++) {
//                 rowsNotSelected[row].style.backgroundColor = "";
//                 rowsNotSelected[row].classList.remove('selected');
//             }


//             // Highlights the selected row
//             var rowSelected = table.getElementsByTagName('tr')[rowId];
//             rowSelected.style.backgroundColor = highlighter;
//             rowSelected.className += "selected";

//             // // TODO: Figure out way to unlight on second click if already highlighted
//             // if (rowSelected.classList.contains("selected")) {
//             //     rowSelected.style.backgroundColor = "";
//             // }
//         }
//     }
// }

function addHighlightAttribute() {
    const table = document.getElementById("ticket-table");
    table.getElementsByTagName('tr').setAttribute('highlight', false);
}

function highlightTicketRow() {
    let highlighter = "#ccff00"
    const table = document.getElementById("ticket-table");

    for (var i = 1; i < table.rows.length; i++) {
        table.rows[i].onclick = function () {
            var rowId = this.parentNode.rowIndex;

            if (!this.highlight) {
                table.getElementsByTagName('tr')[rowId]
                unhighlightTicketRow();
                this.style.backgroundColor = highlighter;
                this.highlight = true;
                this.className += "selected";
            } else {
                this.style.backgroundColor = "";
                this.highlight = false;
            }
        }
    }
}

function unhighlightTicketRow() {
    var table = document.getElementById("ticket-table");
    for (var i = 0; i < table.rows.length; i++) {
        var row = table.rows[i];
        row.style.backgroundColor = "";
        row.highlight = false;
    }
}

function toggleModifier() {
    this.parentNode.style.display = 'none';
}

var menu_buttons = document.getElementsByClassName('btn btn-block menu-button');
for (let i = 0; i < menu_buttons; i++) {
    menu_buttons[i].addEventListener('click', subtotalPrice(), false)
}

const subtotalPrice = function () {
    const tableDiv = document.getElementById("ticket-table");
    const priceDiv = document.getElementById("ticket-total");

    console.log('This function is being called')
    for (let i = 1; i < tableDiv.rows.length; i++) {
        console.log(table.rows[i][2].innerHTML)
        // for (var c = 0, m = table.rows[i].cells.length; c < m; c++) {
        // alert(table.rows[i].cells[c].innerHTML);
    }
    // subtotalSum = table.rows[i].cells[2].innerHTML;
    // price.cell[1].innerHTML = subtotalSum
}

$(document).ready(function() {
    addTicketRow();
    addMenuButton();
})