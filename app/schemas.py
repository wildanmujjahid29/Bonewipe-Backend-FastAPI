from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ========== Category ==========
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# ========== Product ==========
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    stock: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    category: Category  # include nested category info

    class Config:
        orm_mode = True

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True


# ==== Bank ====
class BankBase(BaseModel):
    name: str
    account_number: str

class BankCreate(BankBase):
    pass

class BankOut(BankBase):
    id: int

    class Config:
        orm_mode = True


# ========== Order item ==========
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemOut(OrderItemCreate):
    id: int
    price_at_order: float

    class Config:
        orm_mode = True

# ========== Order ==========
class OrderCreate(BaseModel):
    customer_name: str
    customer_email: Optional[str] = None
    customer_phone: str
    shipping_address: str
    bank_id: int
    transfer_proof: Optional[str] = None
    items: List[OrderItemCreate]

class OrderOut(BaseModel):
    id: int
    customer_name: str
    customer_email: Optional[str]
    customer_phone: str
    shipping_address: str
    transfer_proof: Optional[str]
    status: str
    created_at: datetime
    bank: BankOut  
    items: List[OrderItemOut]

    class Config:
        orm_mode = True

# ========== Tambahan ==========
class OrderDetailOut(OrderOut):
    total: float

class OrderStatusUpdate(BaseModel):
    status: str

