function showCost(taskId) {
	const csrftoken = Cookies.get('csrftoken');

	fetch(checkPaymentUrl, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		mode: 'same-origin',
		body: JSON.stringify({ task_id: taskId }),
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
	.then(data => {
		if (data.success) {
			totalCostStr = "合計金額:" + data.payment_total;
			productCostStr = "商品代金" + data.total_cost;
			deliveryFeeStr = "手数料" + data.delivery_fee;
			if (confirm(totalCostStr + "\n" + productCostStr + "\n" + deliveryFeeStr)) {
				if (confirm("支払い画面に移ります\nよろしいですか？")) {
					window.location.href = `${paymentUrl}${taskId}/`;
				}
			}
		} else {
			alert(data.error_message);
		}
	})
	.catch(error => {
		console.error("Error:", error);
	});
}