console.log("loaded");

const entryForm = document.getElementById("entry-form");
const table = document.getElementById("display-ideas");

entryForm.addEventListener('submit', function (event) 
    {
        event.preventDefault();
	    const form = event.target;
	    const formData = new FormData(form);
	    const data = {};
	    for (let keyValue of formData.entries()) {
	    	data[keyValue[0]] = keyValue[1];
	    }
        eel.write_idea_to_db(data);

        buildTable();
        entryForm.reset();
    })

const removeEntry = (id) => {
    eel.delete_entry(id);
    buildTable();
}

const buildTable = () => {
    const tableRows = document.getElementById("table-rows");
    tableRows.innerHTML = '';
    eel.get_all_ideas()((r) => {
        r.forEach(idea => {
            let newRow = `<tr>
            <th scope="row">${idea[1]}</th>
            <td>${idea[2]}, ${idea[3]}, ${idea[4]}</td>
            <td>${idea[5]}</td>
            <td><button type="button" class="btn btn-danger" onclick="removeEntry(${idea[0]})">X</button></td>
            </tr>`;
            tableRows.innerHTML += newRow;
        });
    });
}

buildTable()