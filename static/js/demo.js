/**
 * Created by root on 11/06/14.
 */

//Configuraciones generales
var nombre_tabla = "#tabla_productos";
var nombre_boton_eliminar = ".delete";
var nombre_formulario_modal = "#frmEliminar";
var nombre_ventana_modal = "#myModal";
//FIn de configuraciones generales

    $(document).on('ready',function(){
       $(nombre_boton_eliminar).on('click',function(e){
           e.preventDefault();
           var Pid = $(this).attr('id');
           var name = $(this).data('name');
           $('#modal_idProducto').val(Pid);
           $('#modal_name').text(name);
       });

       var options = {
           success:function(response)
           {
               if ((rs != response.status)) {
                   alert("Eliminado");
                   var idProd = response.product_id;
                   var elementos = $(nombre_tabla + ' >tbody >tr').length;
                   if (elementos == 1) {
                       location.reload();
                   } else {
                       $('#tr' + idProd).remove();
                       $(nombre_ventana_modal).modal('hide');
                   }
               } else {
                   alert("Hubo un error al aliminar");
                   $(nombre_ventana_modal).modal('hide');
               };
           }
       };

        $(nombre_formulario_modal).ajaxForm(options);

    });