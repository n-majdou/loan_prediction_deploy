  function getCreditHistValue() {
    var uiCredit = document.getElementsByName("uiCredit");
    for(var i in uiCredit) {
      if(uiCredit[i].checked) {
          return parseInt(i) - 1;
      }
    }
    return -1; // Invalid Value
  }

  function onClickedEstimateLoan() {
    console.log("Estimate loan button clicked");
    var applicant_income = document.getElementById("uiAppInc");
    var coapplicant_income = document.getElementById("uiCoappInc");
    var loan_amount = document.getElementById("uiLoanAmt");
    var loan_amount_term = document.getElementById("uiLoanTrm");
    var credit_history = getCreditHistValue();
    var estLoan= document.getElementById("uiEstimatedLoan");

    //var url = "http://127.0.0.1:5000/predict_loan"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/predict_loan";

    $.post(url, {
        applicant_income: parseFloat(applicant_income.value),
        coapplicant_income: parseFloat(coapplicant_income.value),
        loan_amount: parseFloat(loan_amount.value),
        loan_amount_term: loan_amount_term.value,
        credit_history: credit_history
         },function(data, status) {
        console.log(data.loan_or_no_loan);
        estLoan.innerHTML = "<h2>" + data.loan_or_no_loan.toString() + "</h2>";
        console.log(status);
    });
  }

  // things to do when http page is loaded
  function onPageLoad() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_loan_terms"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/get_loan_terms";
    $.get(url,function(data, status) {  // we get repsponse back in data as seen in POSTMAN
        console.log("got response for get_loan_terms request");
        if(data) {
            var loan_terms = data.loan_terms;
            var uiLoanTrm = document.getElementById("uiLoanTrm");
            $('#uiLoanTrm').empty();
            for(var i in loan_terms) {  // a list of locations so we iterate over them 1 by one and put them in drop down
                var opt = new Option(loan_terms[i]);
                $('#uiLoanTrm').append(opt);
            }
        }
    });
  }

  window.onload = onPageLoad;