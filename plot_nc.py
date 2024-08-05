import matplotlib.pyplot as plt 
import xarray as xr 
import cartopy.crs as ccrs

grace_data = xr.open_dataset("data/CSR.nc")

grace_data_nepal = grace_data.sel('lat' = slice(20,30),)

# data.sel(time=slice("2000-01-01", "2000-01-02"))

date = 6497.5

data_for_date = grace_data.sel(time = date)

plt.figure(figsize=(10,5))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()

ax.set_xticks(range(-180,181,60), crs = ccrs.PlateCarree())
ax.set_yticks(range(-90,91,30), crs = ccrs.PlateCarree())

data_for_date['lwe_thickness'].plot()
plt.show()