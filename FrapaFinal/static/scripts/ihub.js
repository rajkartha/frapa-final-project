function init() {
    // Grab a reference to the dropdown select element
    var departments = d3.select("#Departments");
    var aisles = d3.select("#Aisles");
    var products = d3.select("#Products");
  
    // Use the list of sample names to populate the select options
    d3.json("/static/Departments.json").then((data) => {
  
      data.forEach((department) => {
        departments
          .append("option")
          .text(department.Antecedents)
          .property("value", department.Antecedents);
      });
    })
     // Use the list of sample names to populate the select options
     d3.json("/static/Aisles.json").then((data) => {
  
      data.forEach((aisle) => {
        aisles
          .append("option")
          .text(aisle.Antecedents)
          .property("value", aisle.Antecedents);
      });
    })
     // Use the list of sample names to populate the select options
     d3.json("/static/Products.json").then((data) => {
  
      data.forEach((product) => {
        products
          .append("option")
          .text(product.Antecedents)
          .property("value", product.Antecedents);
      });
    })
  
  }
  
  function optionChanged(selection, output) {
    var consequent = d3.select('#'+ output)
    if(output == "Department_C") {
      var data_file = "Departments.json"
    } else if (output == "Aisle_C") {
      var data_file = "Aisles.json"
    } else {
      var data_file = "Products.json"
    }
  
  
  
    d3.json("/static/"+ data_file).then((data) => {
      var filtered_data = data.filter(obj => obj.Antecedents == selection)
      filtered_data.forEach((departments) => {
        consequent
          .html(null)
          .append("p")
          .text(departments.Consequents);
      });
  
  
    })
  
  
  }
  
  // Initialize the dashboard
  init();
  
  