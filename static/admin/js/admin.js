(function($) {
    $(document).ready(function() {
        // Auto-calculate total price
        $('#id_quantity, #id_item').change(function() {
            const itemSelect = $('#id_item option:selected');
            const price = parseFloat(itemSelect.data('price')) || 0;
            const quantity = parseInt($('#id_quantity').val()) || 0;
            const totalPrice = price * quantity;

            $('#id_total_price').val(totalPrice.toFixed(2)); // Update total price field
        });
    });
})(django.jQuery);
