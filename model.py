from keras.models import Sequential, Model
from keras.layers import Bidirectional, CuDNNLSTM, Dropout, Dense, Input
from keras.optimizers import Adam

def create_model(window_size=200):
    input_gyro_acc = Input((window_size, 6))
    lstm1 = Bidirectional(CuDNNLSTM(128, return_sequences=True))(input_gyro_acc)
    
    #drop1 = Dropout(0.25)(lstm1)
    #lstm2 = Bidirectional(CuDNNLSTM(128))(drop1)

    lstm2 = Bidirectional(CuDNNLSTM(128))(lstm1)
    
    #drop2 = Dropout(0.25)(lstm2)    
    #output_delta_l = Dense(1)(drop2)
    #output_delta_psi = Dense(1)(drop2)

    output_delta_l = Dense(1)(lstm2)
    output_delta_psi = Dense(1)(lstm2)

    model = Model(inputs = input_gyro_acc, outputs = [output_delta_l, output_delta_psi])
    model.summary()
    model.compile(optimizer = Adam(0.0001), loss = 'mean_squared_error')
    
    return model