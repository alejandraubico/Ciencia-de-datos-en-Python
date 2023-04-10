CREATE_DW =  """
CREATE TABLE IF NOT EXISTS dimShipStatus(
	ShipStatusID INT NOT NULL AUTO_INCREMENT,
	ShipStatusName VARCHAR(50) 
    PRIMARY KEY(ShipStatusID)
);

CREATE TABLE IF NOT EXISTS dimFulfillment(
	FulfillmentID INT PRIMARY KEY,
	FulfillmentName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimSalesChannel(
	SalesChannelID INT PRIMARY KEY,
	SalesChannelName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimShipService(
    ShipServiceID INT PRIMARY KEY,
    ShipServiceName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimProduct(
    ProductID INT PRIMARY KEY,
    SKU VARCHAR(50) UNIQUE,
    Style varchar(15),
    Category varchar(30),
    Size varchar(10),
    ASIN varchar (15)
);

CREATE TABLE IF NOT EXISTS dimCourierStatus(
    CourierStatusID INT PRIMARY KEY,
    CourierStatusName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimCurrency(
    CurrencyID INT PRIMARY KEY,
    CurrencyName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimPromotion(
    PromotionID INT PRIMARY KEY,
    PromotionName VARCHAR(50) 
);

CREATE TABLE IF NOT EXISTS dimFulfillmentBy(
    FulfillmentByID INT PRIMARY KEY,
    FulfillmentByName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimShippingAddress(
    ShippingAddressID INT PRIMARY KEY,
    ShipCity VARCHAR(100) UNIQUE,
    ShipState VARCHAR(30) UNIQUE,
    ShipZipCode VARCHAR(10) UNIQUE,
    ShipCountry VARCHAR(10) 
);

create table if not exists dimDate(
    DateID date primary key,
    year int,
    semester int, 
    trimester int,
    month int,
    day int     
);

create table if not exists factOrders(
    OrderIndexID varchar(100) primary key,
    DateID date,
    ShipStatusID int,
    FulfillmentID int,
    SalesChannelID int,
    ShipServiceID int,
    ProductID int,
    CourierStatusID int,
    CurrencyID int,
    PromotionID int,
    FulfillmentByID int,
    ShippingAddressID int,
    Quantity varchar(75),
    Amount double,
    B2B varchar(10),

    constraint fk_fact_dimShipStatus
        foreign key (ShipStatusID)
            references dimShipStatus(ShipStatusID),

    constraint fk_fact_dimFulfillment
        foreign key (FulfillmentID)
            references dimFulfillment(FulfillmentID),

    constraint fk_fact_dimSalesChannel
        foreign key (SalesChannelID)
            references dimSalesChannel(SalesChannelID),

    constraint fk_fact_dimShipService
        foreign key (ShipServiceID)
            references dimShipService(ShipServiceID),

    constraint fk_fact_dimProduct
        foreign key (ProductID)
            references dimProduct(ProductID),

    constraint fk_fact_dimCourierStatus
        foreign key (CourierStatusID)
            references dimCourierStatus(CourierStatusID),

    constraint fk_fact_dimCurrency
        foreign key (CurrencyID)
            references dimCurrency(CurrencyID),

    constraint fk_fact_dimPromotion
        foreign key (PromotionID)
            references dimPromotion(PromotionID),

    constraint fk_fact_dimFulfillmentBy
        foreign key (FulfillmentByID)
            references dimFulfillmentBy(FulfillmentByID),

    constraint fk_fact_dimShippingAddress
        foreign key (ShippingAddressID)
            references dimShippingAddress(ShippingAddressID),

    constraint fk_fact_dimDate
        foreign key (DateID)
            references dimDate(DateID)

);
"""