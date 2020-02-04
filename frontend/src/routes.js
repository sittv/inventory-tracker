import HomePage from "./components/HomePage";
import SignedIn from "./components/SignedIn";
import AddUser from "./components/actions/AddUser";
import ListItems from "./components/actions/ListItems";
import AddItem from "./components/actions/AddItem";
import IdCheckout from "./components/actions/IdCheckout";
import BarcodeCheckout from "./components/actions/BarcodeCheckout";
import SetBarcode from "./components/actions/SetBarcode";
import IDReturn from "./components/actions/IDReturn";
import BarcodeReturn from "./components/actions/BarcodeReturn";
import ActionList from "./components/ActionList";

export default [
    {path: "/", component: HomePage},
    {path: "/signed_in", component: SignedIn, children: [
        {path: "", component: ActionList},
        
        {path: "add_user", component: AddUser},
        {path: "list_items", component: ListItems},
        {path: "add_item", component: AddItem},
        {path: "id_checkout", component: IdCheckout},
        {path: "barcode_checkout", component: BarcodeCheckout},
        {path: "set_barcode", component: SetBarcode},
        {path: "id_return", component: IDReturn},
        {path: "barcode_return", component: BarcodeReturn},
    ]},


]